import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get('/account')
def about():
    return {
        'user_name': 'almaz'
    }


@router.get('/account/register')
def register():
    return {
        'user_name': 'almaz'
    }


@router.get('/account/login')
def login():
    return {
        'user_name': 'almaz'
    }
