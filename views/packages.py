import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get('/')
@template(template_file='index.html')
def index():
    return {
        'user_name': 'almaz'
    }


@router.get('/account')
def about():
    return {
        'user_name': 'almaz'
    }
