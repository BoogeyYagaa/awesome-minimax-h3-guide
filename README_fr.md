# Awesome MiniMax H3 Guide · Flyne AI

[![Flyne AI MiniMax H3 field guide](assets/previews/flyne-h3-cover.webp)](assets/flyne-h3-cover.png)

<sub>Couverture éditoriale générée par IA, pas un résultat H3.</sub>

[English](README.md) · [简体中文](README_zh.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md)

[Démarrer avec cinq secondes](docs/quick-start.md) · [Images de référence](docs/reference-gallery.md) · [Guide des prompts](docs/prompting-guide.md) · [12 modèles](templates/README.md) · [Installation locale](docs/deployment-guide.md)

## Utiliser MiniMax H3 sur Flyne AI

| Accès recommandé dans le navigateur | Essai gratuit sans inscription |
|---|---|
| [MiniMax H3](https://flyne.ai/model/minimax-h3/) | [Tester directement en ligne](https://flyne.ai/free-minimax-h3/) |

L’interface gratuite vérifiée le 2026-09-21 propose des vidéos de **5 secondes en 480p**. Commencez par les [exercices courts](docs/quick-start.md).

## Essayer un exercice de cinq secondes

Les exercices FX5 ont été rédigés séparément pour apprendre. Ils ne sont pas les prompts ayant produit les vidéos liées, et leurs résultats ne sont pas encore vérifiés. Les explications détaillées et les exercices sont en anglais et en chinois.

1. Choisissez un exercice FX5 dans la galerie et copiez son prompt en anglais ou en chinois.
2. Ouvrez l’outil gratuit, laissez les champs d’image vides et choisissez le format indiqué.
3. Lancez la génération et effectuez manuellement la vérification demandée. « Queued » signifie que la demande est en attente : gardez la page ouverte sans renvoyer la même demande.
4. Une fois la vidéo disponible, vérifiez les formes, le mouvement et la fin. Contrôlez le son séparément.

[Exercices et vidéos (anglais et chinois)](docs/x-community-showcase.md) · [Flyne AI](https://flyne.ai/free-minimax-h3/)

## Vidéos et prompts de la communauté

12 exemples X avec vidéos, publications originales, courts extraits et commentaires.

[Exercices et vidéos (anglais et chinois)](docs/x-community-showcase.md) · [Exemples officiels](docs/official-h3-examples.md)


## Guide pratique MiniMax H3 pour la production audiovisuelle

Une ressource communautaire Flyne AI : 100 prompts, méthodes de production, choix du modèle et évaluation de la qualité et des coûts. 84 recettes sont réutilisées sous MIT avec attribution ; 16 sont de nouvelles propositions Flyne AI. Ce projet n’a pas vérifié leurs résultats par génération.

[Tous les prompts](prompts/README.md) · [Essayer sur Flyne AI](https://flyne.ai/model/minimax-h3/) · [Guide des modèles](docs/model-guide.md)

## Bien démarrer

Choisissez une recette selon le livrable et définissez le rôle de chaque référence. Utilisez uniquement les entrées acceptées par votre interface. Commencez avec un sujet et une action ; vérifiez la forme, le mouvement et le son. Corrigez un type de défaut à la fois et conservez un journal d’exécution.

[Run record](templates/run-record.json) · [Prompt template](templates/prompt.md)

## Cas d’usage

| ID | Cas d’usage |
|---|---|
| FY-002 | [Variantes de produit](prompts/flyne/fy-002.md) |
| FY-003 | [Assistance client](prompts/flyne/fy-003.md) |
| FY-006 | [Localisation](prompts/flyne/fy-006.md) |
| FY-009 | [Fonds pour sous-titres](prompts/flyne/fy-009.md) |
| FY-016 | [Évaluation des références](prompts/flyne/fy-016.md) |

## Modèles et disponibilité

Au 2026-09-17, les poids de H3-Base sont téléchargeables. H3 Max est une variante hébergée, issue du post-entraînement de fal ; aucun poids public n’a été trouvé dans les sources primaires consultées. Le parcours officiel complet en 2K comprend aussi des composants hébergés. La licence MIT du dépôt est distincte de la Community License du modèle.

[Guide des modèles](docs/model-guide.md) · [Sources](docs/sources.md)

## Documentation et recherche

- [Méthodes de production](docs/workflows.md)
- [Qualité et coûts](docs/evaluation.md)
- [Pistes de valeur future](docs/opportunities.md)
- [Sources](docs/sources.md)

La recherche inclut les exercices FX5 séparément du catalogue. `--origin exercise` limite la recherche aux exercices et `--show-prompt` affiche le texte en anglais et en chinois.

Python 3.9+:

```sh
python3 scripts/catalog.py search "product"
python3 scripts/catalog.py search "FX5-002" --origin exercise --show-prompt
python3 scripts/catalog.py search "FY-002" --show-prompt
python3 scripts/build.py
python3 scripts/validate.py
```

[JSON catalog](data/catalog.json)

## Attribution et participation

Les 84 recettes importées conservent le copyright Flaq AI et la licence MIT d’origine. Une légère reformulation ne constitue pas une nouvelle attribution. Les nouvelles propositions ne sont pas testées. Les README existent en huit langues ; les guides détaillés sont en anglais avec des résumés chinois et les prompts de référence en anglais. Consultez les tarifs, modes et conditions d’accès actuels de Flyne AI.

[Mentions des tiers](THIRD_PARTY_NOTICES.md) · [Contribuer](CONTRIBUTING.md) · [MIT](LICENSE) · [Flaq AI MIT](licenses/Flaq-AI-MIT.txt)

## Devenez partenaire affilié de Flyne AI

Créateurs, formateurs, auteurs de tests et équipes créatives : nous vous invitons à devenir nos partenaires ! Partagez Flyne AI avec votre lien de parrainage et recevez une commission sur les commandes payantes valides et admissibles :

- **20 %** sur la première commande payante valide de l’utilisateur parrainé.
- **10 %** sur ses commandes payantes valides suivantes, passées dans les **60 jours suivant son inscription**.

[Rejoindre le programme d’affiliation Flyne AI](https://flyne.ai/affiliate-program/). L’admissibilité, l’attribution et les versements dépendent de l’accord en vigueur et de la procédure de vérification.

Pour toute question ou proposition de partenariat : [contact@flyne.ai](mailto:contact@flyne.ai).
