from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

from db.databases import databases

from schemas.user import User

from models.dog import Bread
from models.dog import Dog
from models.user import User

app = FastAPI(title='Dogs API')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer('/api/v1/auth/')

databases.create_tables([Bread, Dog, User])

def get_user(db, username: str):
    if username in db:
      pass

def authenticated_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)

@app.post('/api/v1/auth/')
async def auth(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    email, password = form_data.username, form_data.password
    
    try:
        user = User.get(User.email == email)
        if (user.email != None):
            if user.password != password:
                return {"message": 'password is not correct'}
            
            return {"token":form_data.username} 
    except:
      return {"message": 'user no exist'}
    
    # token: str = 'dlsklklskdfldfsflsflsflsfklskflsfklskflsdkfsjfiruisjdklsjksdhfufr'


@app.get('/api/v1/breeds/')
async def get_breeds(page: int = 1, page_size: int = 10, name: str = None, token: str = Depends(oauth2_scheme)):
    breeds = []
    if page < 1 or page_size < 1:
        raise HTTPException(status_code=400, detail="La página y el tamaño de página deben ser mayores a 0.")
    
    skip = (page - 1) * page_size
    limit = page_size
    
    query = Bread.select()
 
    if name != None:
        data = filter(lambda x : x.name == name, query)
        result = [{"id":x.id, "name": x.name} for x in data]
        return {
            "count":len(result),
            "results": result
        }

    query = query.offset(skip).limit(limit)
    for x in query:
        breeds.append({"id": x.id, "name":x.name})
    
    return {
        "count": len(breeds),
        "next": f'http://127.0.0.1:8000/api/v1/breeds/?page={page + 1}&page_size={limit}',
        "previous": f'http://127.0.0.1:8000/api/v1/breeds/?page={1 if page - 1 == 0 else page - 1}&page_size={limit}',
        "results": breeds
    }
    
@app.get('/api/v1/dogs/')
async def get_dogs():
    return {
        "count": 0,
        "next": "http://example.com",
        "previous": "http://example.com",
        "results": [

            {
                "id": 0,
                "name": "string",
                "breed": 0
            }

        ]
    }