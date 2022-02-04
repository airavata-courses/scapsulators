import React from 'react'
import GlobalContext from "./context/GlobalContext"
import Container from "./container"

import './App.css'

export default function App() {

    return (
        <GlobalContext>
        <Container />
        </GlobalContext>
    )
}

