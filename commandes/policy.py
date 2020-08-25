from rest_access_policy import AccessPolicy


class CommandePolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve", "update_moderateur"],
            "principal": ["group:modérateur", "group:administrateur"],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "principal": ["group:administrateur"],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ["group:fournisseur"],
            "effect": "allow"
        },
        {
            "action": ["update_fournisseur", "destroy"],
            "principal": ["group:fournisseur"],
            "effect": "allow",
            "condition": "is_fournisseur"
        }
    ]

    def is_fournisseur(self, request, view, action) -> bool:
        commande = view.get_object()
        return request.user == commande.fournisseur.user

class LivraisonPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve", "create"],
            "principal": ["group:modérateur", "group:administrateur"],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "principal": ["group:administrateur"],
            "effect": "allow"
        },
        {
            "action": ["update_livreur"],
            "principal": ["group:livreur"],
            "effect": "allow",
            "condition": "is_livreur"
        },
        {
            "action": ["ajouter_feedback"],
            "principal": ["group:fournisseur"],
            "effect": "allow",
            "condition": "is_fournisseur"
        },
    ]

    def is_livreur(self, request, view, action) -> bool:
        livraison = view.get_object()
        return request.user == livraison.livreur

    def is_fournisseur(self, request, view, action) -> bool:
        livraison = view.get_object()
        return request.user == livraison.commande.fournisseur.user