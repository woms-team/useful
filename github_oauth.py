from fastapi import FastAPI
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware


# требует Authlib==0.14.2 и httpx==0.13.3

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="!secret")
oauth = OAuth()


oauth.register(
    name='github',
    client_id='ID',
    client_secret='SECRET',
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

@app.route('/')
async def login(request):
    github = oauth.create_client('github')
    redirect_uri = 'http://localhost:8000/github_login'
    return await github.authorize_redirect(request, redirect_uri)

@app.route('/github_login')
async def authorize(request):
    token = await oauth.github.authorize_access_token(request)
    resp = await oauth.github.get('user', token=token)
    profile = resp.json()
    print('*'*10)
    print(profile)
    print('*' * 10)
    return [profile]
