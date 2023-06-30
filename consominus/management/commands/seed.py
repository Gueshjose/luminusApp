from django_seed import Seed    
from consominus.models import Utilisateur, data_user, Contrat,Luminus,Accesory
from django.core.management.base import BaseCommand
from faker import Faker
from random import randint
from pathlib import Path

fake = Faker()

class Command(BaseCommand):
    help = 'Making Seed'
    
    
                
    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()
        
        seeder.add_entity( Utilisateur, 1,{                
                'name':fake.name() ,
                'mail':fake.ascii_free_email(),
                'image': "images/client.png",
                'numeroClient' : fake.pystr(),
                'gsm':fake.phone_number(),
                'conseillé':fake.name()
        })
        
        inserted_pks = seeder.execute()
        print(inserted_pks)
        
        seeder.add_entity(Luminus,1,{
            'green': randint(0,100),
            'grey': randint(0,100)
        })
        
        seeder.add_entity(Contrat,1,{
            'tarifHoraire':1.5,
            'typeContrat': 'TOP-4',
            'user': Utilisateur.objects.get(id=1),
        })
        
        seeder.add_entity(data_user,1,{
            'prod': randint(0,100),
            'conso':randint(0,100),
        })
        
        seeder.add_entity(Accesory,1,{
            'domotique': False,
        })
        
        inserted_pks = seeder.execute()
        print(inserted_pks)
        
