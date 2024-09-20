from server.app import app, db
from server.models import Animal, Zookeeper, Enclosure

class TestApp:
    @classmethod
    def setup_class(cls):
        """Set up test data before running tests."""
        with app.app_context():
            # Create the database tables
            db.create_all()
            
            # Create test instances
            a_1 = Animal(name="Lion", species="Panthera leo")
            a_2 = Animal(name="Tiger", species="Panthera tigris")
            e = Enclosure(environment="Grass", open_to_visitors=True)
            z = Zookeeper(name="John Doe", birthday="1985-01-01")
            
            # Set up relationships
            e.animals = [a_1, a_2]
            z.animals = [a_1, a_2]
            
            # Add to session and commit
            db.session.add_all([a_1, a_2, e, z])
            db.session.commit()
