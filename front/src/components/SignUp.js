import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import { useMutation } from "@apollo/react-hooks";
import { useCookies } from "react-cookie";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import gql from "graphql-tag";

const ADD_USER = gql`
  mutation AddUser($username: String!, $password: String!, $email: String!) {
    addUser(
      input: { username: $username, password: $password, email: $email }
    ) {
      user {
        id
      }
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

export function SignUp() {
  const classes = useStyles();
  const [user, setUser] = useState({});
  const [addUser, { data }] = useMutation(ADD_USER, {
    ignoreResults: false,
    onCompleted: ({ addUser }) => {}
  });

  const handleSubmit = ev => {
    ev.preventDefault();
    addUser({ variables: user });
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
        id="email"
        required
        label="Email"
        className={classes.textField}
        margin="normal"
        type="email"
        variant="outlined"
        onChange={e => changeProperty(e, "email")}
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
        Sign Up
      </Button>
    </form>
  );
}
