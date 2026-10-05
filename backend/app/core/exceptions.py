class ApplicationError(Exception):
    code = "APPLICATION_ERROR"

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class SourceNotFound(ApplicationError):
    code = "SOURCE_NOT_FOUND"


class DuplicateSource(ApplicationError):
    code = "DUPLICATE_SOURCE"


class InvalidTaxonomyCode(ApplicationError):
    code = "INVALID_TAXONOMY_CODE"


class InvalidEvidence(ApplicationError):
    code = "INVALID_EVIDENCE"


class ProductKnowledgeNotFound(ApplicationError):
    code = "PRODUCT_KNOWLEDGE_PENDING"


class IntelligencePipelineError(ApplicationError):
    code = "INTELLIGENCE_PIPELINE_ERROR"

