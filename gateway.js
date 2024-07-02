const {ApolloServer} = require('apollo-server');
const {ApolloGateway, IntrospectAndCompose} = require('@apollo/gateway');

const gateway = new ApolloGateway({
    supergraphSdl: new IntrospectAndCompose({
        subgraphs: [
            {name: 'users', url: 'http://localhost:8000/graphql'},
            {name: 'posts', url: 'http://localhost:8001/graphql'},
        ],
    }),
});

const server = new ApolloServer({
    gateway,
    subscriptions: false,
    cors: {
        origin: '*',
        credentials: true,
    },
});

server.listen().then(({url}) => {
    console.log(`🚀 Gateway ready at ${url}`);
}).catch(err => {
    console.error('❌ Error starting server:', err);
});
