from marshmallow import Schema, fields

# dump_only=True means that the data should only be returned by the request response.

# required=True means that the data should be part of the JSON payload received as part of the request.

# class ItemSchema(Schema):
#     id = fields.Str(dump_only=True)
#     name = fields.Str(required=True)
#     price = fields.Float(required=True)
#     store_id = fields.Str(required=True)


# class ItemUpdateSchema(Schema):
#     name = fields.Str()
#     price = fields.Float()


# class StoreSchema(Schema):
#     id = fields.Str(dump_only=True)
#     name = fields.Str(required=True)

class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

# load_only – Fields to skip during serialization (write-only fields)
# This means that we are going to be able to pass in the store_id when we are 
#  receiving data from the client.

# dump_only – Fields to skip during deserialization (read-only fields)
# This means the nested store will only be determined for returning data to the client.
class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

# dump_only – Fields to skip during deserialization (read-only fields)
# This means the nested items will only be determined for returning data to the client.
class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)