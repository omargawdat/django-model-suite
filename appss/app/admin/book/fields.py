class BookFields:
    ID = "id"
    TITLE = "title"
    AUTHOR = "author"
    PUBLICATION_DATE = "publication_date"
    NUM_PAGES = "num_pages"
    IS_BORROWED = "is_borrowed"

    @classmethod
    def get_field_name(cls, model, field):
        return model._meta.get_field(field).name