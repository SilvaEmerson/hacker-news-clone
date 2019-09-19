import React from "react";
import ReactDOM from "react-dom";
import { MockedProvider } from "@apollo/react-testing";
import { Login, GET_USER_TOKEN } from "./Login";

const mocks = [
  {
    request: {
      query: GET_USER_TOKEN,
      variables: {
        username: "demo",
        password: "demo"
      }
    },
    result: {
      data: {
        token: "dasdsdasdasds"
      }
    }
  }
];

it("renders without crashing", () => {
  const div = document.createElement("div");
  ReactDOM.render(
    <MockedProvider mocks={mocks} addTypename={false}>
      <Login />
    </MockedProvider>,
    div
  );
  ReactDOM.unmountComponentAtNode(div);
});
