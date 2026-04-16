# B001 app

## BPL

### 🥈 Jour 2 — State & Events - 🥉 Jour 3 — Navigation & Routing

**Cookbooks à étudier :**

* [ ] **Objectif :** comprendre comment Flet gère l’état et pourquoi FletX sera utile.

* [ ] on_click / on_change / on_submit :
  * [/] [Declarative vs imperative CRUD app](http://localhost:3000/docs/cookbook/declarative-vs-imperative-crud-app)
  * [ ] [Drag and drop](http://localhost:3000/docs/cookbook/drag-and-drop)
  * [ ] [Keyboard shortcuts](http://localhost:3000/docs/cookbook/keyboard-shortcuts)

* [ ] page.update() & Timers, async, futures :
  * [ ] [Async apps](http://localhost:3000/docs/cookbook/async-apps)
  * [ ] [Large lists](http://localhost:3000/docs/cookbook/large-lists)

### Comment Flet gère l’état

* [ ] [PubSub](http://localhost:3000/docs/cookbook/pub-sub)
* [ ] [Subprocess](http://localhost:3000/docs/cookbook/subprocess)
* [ ] → Avoir compris pourquoi `page.update()` devient vite lourd

### Comment organiser un minimum la logique

* [ ] [Navigation and routing](http://localhost:3000/docs/cookbook/navigation-and-routing)
* [ ] [Adaptive apps](http://localhost:3000/docs/cookbook/adaptive-apps)

### À voir à l’occasion (autres cookbooks utiles)

* [x] [Expanding Controls](http://localhost:3000/docs/cookbook/expanding-controls)
* [x] [Colors](http://localhost:3000/docs/cookbook/colors)
* [x] [Assets](http://localhost:3000/docs/cookbook/assets)
* [x] [Fonts](http://localhost:3000/docs/cookbook/fonts) (#09)
* [/] [Theming](http://localhost:3000/docs/cookbook/theming)

---

* [ ] [Accessibility](http://localhost:3000/docs/cookbook/accessibility)
* [ ] [Control Refs](http://localhost:3000/docs/cookbook/control-refs)
* [ ] [Custom Controls](http://localhost:3000/docs/cookbook/custom-controls)
* [ ] [Read and Write Files](http://localhost:3000/docs/cookbook/read-and-write-files)
* [ ] [Client storage](http://localhost:3000/docs/cookbook/client-storage)
* [ ] [Session storage](http://localhost:3000/docs/cookbook/session-storage)
* [ ] [Logging](http://localhost:3000/docs/cookbook/logging)
* [ ] [Authentication](http://localhost:3000/docs/cookbook/authentication)
* [ ] [Animations](http://localhost:3000/docs/cookbook/animations)
* [ ] [Encrypting sensitive data](http://localhost:3000/docs/cookbook/encrypting-sensitive-data)

---

### 🏅 Jour 4 — Controls avancés

* [ ] **Objectif :** donner de la valeur à ton app avec des composants puissants.

**Cookbooks à étudier :**

* [ ] ListView / GridView
* [ ] DataTable
* [ ] Dialogs / Snackbars / BottomSheets
* [ ] Tabs / ExpansionTile / NavigationRail

**À retenir :**

* [ ] Afficher des listes dynamiques
* [ ] Créer des dialogues propres
* [ ] Structurer des écrans complexes

**À ignorer :**

* [ ] Dashboards trop avancés
* [ ] DataTables ultra*complexes

### 🏆 Jour 5 — Files, Storage, HTTP, Async

* [ ] **Objectif :** connecter ton app au monde réel.

**Cookbooks à étudier :**

* [ ] FilePicker / upload / download
* [ ] Local storage (page.client_storage)
* [ ] HTTP requests (GET/POST)
* [ ] Async tasks

**À retenir :**

* [ ] Stockage local
* [ ] Appels API
* [ ] Gestion propre de l’async

**À ignorer :**

* [ ] Streaming avancé
* [ ] Upload multi*fichiers complexes

---

### 🚀 Prochaines étapes (après les 5 jours)

* [ ] MVP 20 → 25/04

  (Garder rytme 1 cookbook ouis 1 ref flet / j.)

#### **Jours 6–7 : Construire ton prototype Flet**

* [ ] 2–3 écrans
* [ ] Navigation simple
* [ ] Stockage local
* [ ] Logique métier minimale

#### **Jours 8–10 : Migration vers FletX**

* [ ] Installer FletX
* [ ] Comprendre Rx (réactivité)
* [ ] Créer controllers + services
* [ ] Routing avancé
* [ ] Structurer ton app proprement
* [ ] Utiliser la CLI (`fletx new`, `fletx run`)

À la fin du jour 10 :  
➡️ [ ] Tu as une app structurée, propre, scalable, prête à être vendue.

### 🥇 Jour 1 — Layout & Responsive Design

* [ ] **Objectif :** maîtriser la base visuelle pour créer des interfaces propres et harmonieuses.

**Cookbooks à étudier :**

* [x] Layout basics (Row, Column, Container, Stack)
* [x] ResponsiveRow
* [x] Expand / Flexible / alignment / spacing / Wraping
* [x] Padding / margin / border radius / shadows

**À retenir :**

* [x] `expand=1` pour gérer l’espace
* [x] Différence entre `alignment` (-1, -1) → (1, 1) et `horizontal_alignment` (MainAxis & CrossAxis)
* [x] Quand utiliser `Stack`
* [x] Construire des layouts fluides et responsives

**À ignorer :**

* [x] Exemples trop complexes ou décoratifs
* [x] Styles exotiques (gradients, transforms)

## Run the doc website

```bash
yarn start
```

## Run the app

### uv * [ ] Alternative à pip + env + flet run

Outil **ultra‑rapide** et minimaliste pour installer, exécuter et gérer des environnements.

Run as a desktop app:

```bash
uv run **active flet run *r
uv run **active flet run script.py *r
```

Run as a web app:

```bash
uv run flet run **web *r
```
Option *r => Phone: http://<IP*de*votre*PC>:8550
(Voir avec ipconfig → Carte réseau sans fil Wi*Fi : IPv4)

***

Option 2 — Application Flet sur le téléphone (rendu natif identique à l'APK) ★

Installez l'application Flet depuis le Play Store. Puis lancez en local:

uv run flet run **web **host 0.0.0.0 **port 8550 *r
uv run flet run **web **host 192.168.80.205 **port 8550 *r

Avantages: rendu 100% fidèle à l'APK, hot reload, aucun build
Limite: l'app Flet doit être installée une fois sur le téléphone

Construire apk

```bash
uv run flet build apk *v
```

C:\gsm\build\flutter\android\app\build.gradle.kts

  → Vérifier val resolvedMinSdk = 24

et ajouter en fin de fichier :

// Work around AGP/Kotlin lint crashes in some Flutter plugins during release APK builds.
subprojects {
    tasks.matching {
        it.name == "lintVitalAnalyzeRelease" ||
            it.name == "lintAnalyzeRelease" ||
            it.name == "lintRelease"
    }.configureEach {
        enabled = false
    }
}

Avant :

tasks.register<Delete>("clean") {
    delete(rootProject.layout.buildDirectory)
}

* [ ] [ ] Voir la procédure exacte pour signer le fichier APK généré →  GgleStore

Pour savoir quel Py est utilisé par uv

```bash
 uv run python *c "import sys; print(sys.executable)"
```

For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/getting*started/).

## Build the app ONLY from C:\

### Android

```bash
flet build apk *v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```bash
flet build ipa *v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```bash
flet build macos *v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```bash
flet build linux *v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```bash
flet build windows *v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).

***

```bash
+*******************************************************+
|                       PAGE                            |
|  +**************** Row (center) *******************+  |
|  |  +************** Container *******************+ |  |
|  |  | width=250 or expand                        | |  |
|  |  |  +************ Column *******************+ | |  |
|  |  |  |  [ self.title ]                       | | |  |
|  |  |  |                                       | | |  |
|  |  |  |  [ new_task ] [ add_btn ]             | | |  |
|  |  |  |                                       | | |  |
|  |  |  |  [ tasks_view ]                       | | |  |
|  |  |  +***************************************+ | |  |
|  |  +********************************************+ |  |
|  +*************************************************+  |
+*******************************************************+
```
tip : 

Pour uignorer un faux positif des hints flet
# type: ignore 
