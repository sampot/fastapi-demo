import imp
from dependency_injector import containers, providers

from domain.repositories import user_repository
from repositories.sa_use_case_context import SAUseCaseContext

from repositories.sa_user_repository import SAUserRepository


class Container(containers.DeclarativeContainer):

    uc_context = providers.Singleton(
        SAUseCaseContext
    )

    # Repositories
    user_repository = providers.Singleton(
        SAUserRepository,
        uc_context
    )