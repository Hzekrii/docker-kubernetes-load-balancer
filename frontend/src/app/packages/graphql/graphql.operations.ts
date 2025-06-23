import { gql } from '@apollo/client/core';

export const LOGIN_MUTATION = gql`
  mutation Login($input: LoginInput!) {
    login(input: $input) {
      ... on AuthSuccess {
        token
        user {
          id
          username
          email
        }
      }
      ... on AuthError {
        message
      }
    }
  }
`;

export const REGISTER_MUTATION = gql`
  mutation Register($input: UserInput!) {
    register(input: $input) {
      ... on AuthSuccess {
        token
        user {
          id
          username
          email
        }
      }
      ... on AuthError {
        message
      }
    }
  }
`;