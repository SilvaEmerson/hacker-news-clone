import React from "react";
import { SignUp } from "./components/SignUp";
import { Login } from "./components/Login";
import { ApolloProvider } from "react-apollo";
import { CookiesProvider } from "react-cookie";
import ApolloClient from "apollo-boost";

const endpoint = process.env.REACT_APP_API_ENDPOINT;
const client = new ApolloClient({
  uri: endpoint
});

function App() {
  return (
    <ApolloProvider client={client}>
      <CookiesProvider>
        <header></header>
        <main>
          <Login />
        </main>
        <footer></footer>
      </CookiesProvider>
    </ApolloProvider>
  );
}

export default App;
