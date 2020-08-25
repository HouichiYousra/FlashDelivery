from rest_access_policy import AccessPolicy


class UserPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve", "update", "partial_update", "destroy", "create"],
            "principal": ["group:administrateur"],
            "effect": "allow"
        },
    ]


class FournisseurPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve", "update", "partial_update", "destroy"],
            "principal": ["group:administrateur"],
            "effect": "allow"
        },
    ]