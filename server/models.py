from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class PetOwner(db.Model, SerializerMixin):

    __tablename__ = 'pet_owners'

    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String, nullable=False)
    pet_name = db.Column(db.String, nullable=False)
    pet_type = db.Column(db.String, nullable=False)

    pet_sitters = db.relationship('PetSitter', secondary='appointments', back_populates='pet_owners')
    appointments = db.relationship('Appointment', back_populates='pet_owner', cascade='all, delete_orphan')

    serialize_only = ('id', 'owner_name', 'pet_name', 'pet_type')

    


class PetSitter(db.Model, SerializerMixin):
    # from sqlalchemy import func

    __tablename__ = 'pet_sitters'

    id = db.Column(db.Integer, primary_key=True)
    sitter_name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)

#     def avg_rating(self):
#         from sqlalchemy import func

#         rating = db.session.query(func.avg(Appointment.rating)).filter(

#             Appointment.pet_sitter_id == self.id).filter(
#                 Appointment.rating != None).scalar()
#         return round(rating, 2) if rating else None
    
#     pet_owners = db.relationship('PetOwner', secondary='appointments', back_populates='pet_sitters')
#     appointments = db.relationship('Appointment', back_populates='pet_sitter', cascade='all, delete_orphan')
    
#     serialize_only = ('id', 'sitter_name', 'location', 'price')


        



class Appointment(db.Model, SerializerMixin):

    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Integer, nullable=True, default=None)

    pet_owner_id = db.Column(db.Integer, db.ForeignKey('pet_owners.id'), nullable=False)
    pet_sitter_id = db.Column(db.Integer, db.ForeignKey('pet_sitters.id'), nullable=False)

#     pet_owner = db.relationship('PetOwner', back_populates='appointments')
#     pet_sitter = db.relationship('PetSitter', back_populates='appointments')

#     status = db.Column(db.String, nullable=False)

#     serialize_only = ('id', 'date', 'duration', 'rating', 'status', 'pet_owner_id', 'pet_sitter_id')








# class PetOwnerPetSitter(db.Model):

#     __tablename__ = 'pet_owner_pet_sitter'

#     pet_owner_id = db.Column(db.Integer, db.ForeignKey('pet_owners.id'), primary_key=True)
#     pet_sitter_id = db.Column(db.Integer, db.ForeignKey('pet_sitters.id'), primary_key=True)
#     status = db.Column(db.String, nullable=False)

#     pet_owner = db.relationship('PetOwner', back_populates='pet_sitters')
  
#     pet_sitter = db.relationship('PetSitter', back_populates='pet_owners')
  

     
 










# from sqlalchemy_serializer import SerializerMixin
# from sqlalchemy.ext.associationproxy import association_proxy

# from config import db

# # Models go here!
# 