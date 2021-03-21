deploy:
	cd cdk-angular-template \
		&& npm install \
		&& ng build
	cdk deploy