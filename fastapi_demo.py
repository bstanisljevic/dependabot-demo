from fastapi import FastAPI
from fastapi.routing import APIRouter

app = FastAPI()

router = APIRouter()


@router.get("/")
def index():
    return "Hello, world!"


router.add_route('GET', '/users/{user_id}', UserView.as_view('user'))
router.add_api_route('GET', '/api/users/{user_id}', UserView.as_view('user'))
router.add_view(UserView.as_view('user'))

app.include_router(router)

if __name__ == "__main__":
    app.run(debug=True)
