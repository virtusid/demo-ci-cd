# OpenShift Demo App

Simple Flask app untuk demo deployment di OpenShift.

## Struktur

```
demo-app/
├── app.py            # Flask application
├── requirements.txt  # Python dependencies
├── Dockerfile        # Container image
├── openshift.yaml    # Semua manifests (ImageStream, BuildConfig, Deployment, Service, Route)
└── templates/
    └── index.html    # UI
```

## Endpoints

| Path | Description |
|------|-------------|
| `/` | Landing page |
| `/health` | Readiness/liveness probe |
| `/info` | App info (JSON) |

## Deploy ke OpenShift

```bash
# 1. Login
oc login --token=<token> --server=https://<ocp-api>:6443

# 2. Buat project
oc new-project demo-project

# 3. Buat webhook secret
oc create secret generic github-webhook-secret \
  --from-literal=WebHookSecretKey=<your-secret-token>

# 4. Update git URL di openshift.yaml, lalu apply
oc apply -f openshift.yaml

# 5. Trigger build pertama
oc start-build demo-app --follow

# 6. Ambil URL aplikasi
oc get route demo-app
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `8080` | Port aplikasi |
| `ENVIRONMENT` | `development` | Label environment |
