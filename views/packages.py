import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.packages.details_viewmodel import DetailsViewModel

router = fastapi.APIRouter()


@router.get('/project/{package_name}')
@template(template_file='packages/details.pt')
async def details(package_name: str, request: Request):
    vm = DetailsViewModel(package_name, request)
    await vm.load()

    return vm.to_dict()


@router.get('/account')
def about():
    return {
        'user_name': 'almaz'
    }
