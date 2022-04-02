import React, {useState} from 'react';
import plotImage from '../assets/newimg.gif'
import { MdClose } from 'react-icons/md';
import styled from 'styled-components';
import {Circles} from 'react-loader-spinner';


const CloseModalButton = styled(MdClose)`
  cursor: pointer;
  position: absolute;
  top: 20px;
  right: 20px;
  width: 32px;
  height: 32px;
  padding: 0;
  z-index: 10;
  color: red;
`;



function Dataplot({showModal, openModal, data, loading, setLoading, setData}) {

 
  function handleClick () {
    openModal();
    setLoading(true);
    setData('');
  }

  return <> { showModal ? <div style={plotStyle}>
      {loading == false ? <CloseModalButton
                aria-label='Close modal'
                onClick={handleClick}
              />: <div></div>}
     {/* <img src={`data:image/png;base64,${image}`} />  */}
     {loading === true ? <Circles color="#9deff2" height={80} width={80} /> :<img src={`data:image/png;base64,${data}`}/>}
       </div>: null} </>;
}

export default Dataplot;

const plotStyle = {
display: 'flex',
justifyContent: 'center',
alignItems: 'center',
height: '100vh',
position: 'fixed',
left: 0,
right: 0,
top: 0,
bottom: 0,
zIndex: 10,
background: 'rgba(0, 0, 0, 0.8)',
}
