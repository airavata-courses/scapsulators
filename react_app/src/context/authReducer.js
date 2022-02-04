const authReducer = (state, action) => {
    switch (action.type) {
      case "LOGOUT":
        return {
          ...state,
          user: null,
          loading: false,
        };
      case "LOGIN":
        return {
          ...state,
          user: action.user,
          loading: false,
          error: null,
        };
      case "ERROR":
        return {
          ...state,
          error: action.error,
          loading: false,
        };
      default:
        return state;
    }
  };
  
  export default authReducer;