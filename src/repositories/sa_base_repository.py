from shared.domain import Repository
from src.repositories.sa_use_case_context import SAUseCaseContext


class SABaseRepository(Repository):
    def __init__(self, uc_context: SAUseCaseContext) -> None:
        super().__init__()
        self.uc_context = uc_context
        print('uc_context set')
