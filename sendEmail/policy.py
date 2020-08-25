from rest_access_policy import AccessPolicy


class EmailPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ["group:modérateur", "group:administrateur"],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "principal": ["*"],
            "effect": "deny"
        },
        {
            "action": ["destroy"],
            "principal": ["group:admin"],
            "effect": "allow"
        }
    ]