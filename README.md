# Program-Generator

Generate fast project for

- Angular
- React
- NodeJS (Express)
- NX
- Laravel
- Ionic

## Angular

Generate Angular project with :

- SCSS for styles
- Routing
- Disable strict mode

``
ng new " + projectName +
" --style=scss --routing --strict"
``

## React

Generate React project

``
npx create-react-app " + projectName
``

## NodeJS

Generate NodeJS project with a ```server.js``` file with :

- Express
- Axios
- Nodemon
- Template code with default route and server listening

``
npm init -y
``

## NX

Generate NX project with :

- Angular + Nest
- ```front``` for app name
- SCSS for styles
- No nx-cloud

``
npx create-nx-workspace --preset=angular-nest --appName=front --style=scss --nx-cloud=N " + projectName
``

## Laravel

Generate Laravel project

``
composer create-project laravel/laravel " + projectName + " --prefer-dist"
``

## Ionic

Generate Ionic project

``
ionic start " + projectName + " blank --type=angular"
``