from flask import Flask 
from flask_restful import Api, Resource, reqparse, abort, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # declare the Flask app
api = Api(app) # wrap our app into the API

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/database.db'
db = SQLAlchemy(app) # wrap our app into SQLAlchemy

# define model
class video_models(db.Model):
    
    # define all the fields to be in the model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"(Video(name={name}, views={views}, likes={likes})"
  
# DELETE THIS AFTER FIRST RUN  
# db.create_all()


names = {
    "Tim": {
        "age":20,
        "gender":"male"
    },
    "Jake":{
        "age":20,
        "gender":"male"
    },
}

videos = {}

video_put_args = reqparse.RequestParser() # create new request parser object
video_put_args.add_argument("name", type=str, help="Name of video", required=True)
video_put_args.add_argument("likes", type=int, help="Number of likes", required=True)
video_put_args.add_argument("views", type=int, help="number of views", required=True)


video_update_arguments = reqparse.RequestParser()
video_update_arguments.add_argument("name", type=str, help="Name of video")
video_update_arguments.add_argument("likes", type=int, help="Number of likes")
video_update_arguments.add_argument("views", type=int, help="Number of views")

# declaring resource fields
# make the dictionary to return if we can return a specific object
resource_fields = {
    'id':fields.Integer,
    'name':fields.String,  
    'views':fields.Integer,
    'likes':fields.Integer
}

# def abort_if_video_id_doesnt_exist(video_id):
    # if video_id not in videos:
        # abort(404, description="Video ID is not valid...")
        
# def abort_if_video_exists(video_id):
    # if video_id in videos:
        # abort(409, description="The video you tried to create already exists...")

class Video(Resource): 
    # return something
    @marshal_with(resource_fields)
    def get(self, video_id):
        # abort_if_video_id_doesnt_exist(video_id)
        result = video_models.query.filter_by(id=video_id).first()
        
        if not result:
            abort(404, message="Could not find the requested video ID...")
        
        #return videos[video_id]
        return result
    
    # patch => update something
    # create something
    @marshal_with(resource_fields)
    def put(self, video_id):
        # put data
        # 1. reqparse will validate the validity of data
        # abort_if_video_exists(video_id) 
        # args = video_put_args.parse_args()        
        # videos[video_id] = args        
        # return videos[video_id], 201 # 201 is code for created or 200 means okay
        
        args = video_put_args.parse_args()       
        result = video_models.query.filter_by(id=video_id).first()
        
        if result:
            abort(409, message="This video id has already been taken...")
            
        video = video_models(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        # commit to db
        db.session.add(video)
        db.session.commit()
        return video, 201
        
    def delete(self, video_id):
        # delete video
        del videos[video_id]
        return '', 204
        
    # standard to update the video
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_arguments.parse_args()
        result = video_models.query.filter_by(id=video_id).first() # this is an instance
        
        if not result:
            abort(404, message="Could not update object that doesn't exist")
        
        if args['name']:
            result.name=args['name']
        if args['views']:
            result.views=args['views']
        if args['likes']:
            result.likes=args['likes']
        
        db.session.commit()
        return result

class HelloWorld(Resource):
    def get(self, name):
        return names[name]
        
    def post(self):
        return {"data":"post message"}

api.add_resource(HelloWorld, "/helloworld/<string:name>") # define type of parameter e.g. type string after hello world
api.add_resource(Video, "/Video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True) 
    # going to see all output and information
    # NEVER DO IN PRODUCTION
    
    