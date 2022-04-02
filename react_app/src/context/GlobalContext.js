import React,{createContext,useReducer,useEffect,useState,useContext} from 'react'
import authReducer from './authReducer'
const Global = createContext();

const initialState = {
	user:null,
	error:null,
	loading:true
}

export const useAuth = () => useContext(Global);

const GlobalContext = ({children}) => {
	const [state, dispatch] = useReducer(authReducer, initialState)


	function login({user}){
        console.log(user);
        dispatch({type:"LOGIN",user:user});
	}

    
	// useEffect(()=>{
	// 	login({username:null})
	// },[])
    
	function logout(){
		dispatch({type:"LOGOUT"});
	}

	const value = {login,logout,state}
	return (
		<Global.Provider value={value}>
			{children}
		</Global.Provider>
	)
}

export default GlobalContext