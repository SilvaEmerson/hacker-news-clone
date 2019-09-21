import React from "react";
import ReactDOM from "react-dom";
import { MockedProvider } from "@apollo/react-testing";
import { Login, GET_USER_TOKEN } from "./Login";
import { act } from "react-dom/test-utils";

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

describe("Login component tests", () => {
  let div = null;

  beforeEach(() => (div = document.createElement("div")));

  afterEach(() => {
    ReactDOM.unmountComponentAtNode(div);
    div = null;
  });

  it("renders without crashing", () => {
    ReactDOM.render(
      <MockedProvider mocks={mocks} addTypename={false}>
        <Login />
      </MockedProvider>,
      div
    );
  });

  it("component content should contain 'Login'", () => {
    ReactDOM.render(
      <MockedProvider mocks={mocks} addTypename={false}>
        <Login />
      </MockedProvider>,
      div
    );

    expect(div.textContent).toContain("Login");
  });

  it("component content should contain 'Sucess' message after form submiting", () => {
    act(() => {
      ReactDOM.render(
        <MockedProvider mocks={mocks} addTypename={false}>
          <Login />
        </MockedProvider>,
        div
      );
    });

    let subBtn = div.querySelector("[type=submit]");
    let usernameInput = div.querySelector("[type=text]");
    let passwordInput = div.querySelector("[type=password]");

    usernameInput.textContent = "demo";
    passwordInput.textContent = "demo";

    act(() => {
      subBtn.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    });

    expect(div.textContent).toContain("Login");
  });
});
