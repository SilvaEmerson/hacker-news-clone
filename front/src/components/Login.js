import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import { useMutation } from "@apollo/react-hooks";
import { useCookies } from "react-cookie";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import gql from "graphql-tag";

export const GET_USER_TOKEN = gql`
  mutation GetUserToken($username: String!, $password: String!) {
    tokenAuth(input: { username: $username, password: $password }) {
      token
    }
  }
`;

const useStyles = makeStyles(theme => ({
  container: {
    marginTop: theme.spacing(8),
    display: "flex",
    alignItems: "center",
    flexDirection: "column"
  },
  textField: {
    marginLeft: theme.spacing(1),
    marginRight: theme.spacing(1)
  }
}));

export function Login() {
  const classes = useStyles();
  const [_, setCookie] = useCookies(["user-token"]);
  const [user, setUser] = useState({});
  const [wasLoggedSuccesfully, setWasLoggedSuccessfully] = useState(null);
  const [getUserToken] = useMutation(GET_USER_TOKEN, {
    onCompleted: ({ tokenAuth }) => {
      setCookie("user-token", tokenAuth.token);
      setWasLoggedSuccessfully(s => true);
    },
    onError: err => setWasLoggedSuccessfully(false)
  });
  const handleSubmit = ev => {
    ev.preventDefault();
    getUserToken({ variables: user });
  };
  const changeProperty = (ev, prop) => {
    ev.preventDefault();
    ev.persist();
    setUser(u => ({ ...u, [prop]: ev.target.value }));
  };

  return (
    <form className={classes.container} onSubmit={handleSubmit}>
      <TextField
        id="username"
        required
        label="Username"
        className={classes.textField}
        margin="normal"
        variant="outlined"
        onChange={e => changeProperty(e, "username")}
      />
      <TextField
        id="password"
        required
        label="Password"
        className={classes.password}
        margin="normal"
        type="password"
        variant="outlined"
        onChange={e => changeProperty(e, "password")}
      />
      <Button type="submit" variant="contained" color="primary">
        Login
      </Button>
      {wasLoggedSuccesfully !== null ? (
        wasLoggedSuccesfully ? (
          <h1> Sucess </h1>
        ) : (
          <h1>username or password incorrects</h1>
        )
      ) : null}
    </form>
  );
}
