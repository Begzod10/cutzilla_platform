from models.base import BaseModel
from models.users import User
from models.barber import Barber, BarberService, BarberSchedule, BarberScheduleDetail, BarberServiceScore
from models.client import Client, ClientRequest, ClientRequestService, ClientFavouriteBarbers
from models.service import Service, ServiceImage
from models.region import Country, Region, City
from models.settings import SystemSetting

# This guarantees all models are loaded before Alembic metadata is grabbed
