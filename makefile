run-deploy-docker: run-build-image
	docker run -d --rm --name sl-api \
	-p 8070:8080 \
	-v "${PWD}/sl-api:/app/sl-api" \
	sl-api:1.0 && \
	echo '--------------------------------' && \
	echo "API-URL: http://localhost:8070" && \
	echo '--------------------------------' 


delete-deploy-doker:
	docker stop sl-api


run-deploy-dcompose:
	docker-compose up -d && \
	echo '--------------------------------' && \
	echo "API-URL: http://localhost:8090" && \
	echo '--------------------------------'


delete-deploy-dcompose:
	docker-compose down -v


run-deploy-k8s: create-local-k8s
	cd sl-api-k8s; \
	kubectl --context k3d-k8s-local apply -k k8s-local; \
	sleep 10; \
	nohup kubectl --context k3d-k8s-local -n sl-api port-forward svc/svc-sl-api 8080 & \
	echo '--------------------------------'; \
	echo "API-URL: http://localhost:8080"; \
	echo '--------------------------------'; \
	echo; echo


delete-deploy-k8s:
	cd sl-api-k8s && \
	kubectl --context k3d-k8s-local delete -k k8s-local


run-build-image:
	docker build -t sl-api:1.0 .


create-local-k8s:
	cd k8s-local && \
	bash create_cluster.sh && \
	echo "Wait a moment to build the cluster" 


delete-local-k8s: delete-deploy-k8s
	cd k8s-local && \
	bash delete_cluster.sh
