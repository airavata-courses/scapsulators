import React from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';

export const SidebarData = [
  {
    title: 'Home',
    path: '/home',
    icon: <AiIcons.AiFillHome />,
    cName: 'nav-text'
  },
  // {
  //   title: 'Reports',
  //   path: '/home',
  //   icon: <IoIcons.IoIosPaper />,
  //   cName: 'nav-text'
  // },
  // {
  //   title: 'Products',
  //   path: '/home',
  //   icon: <FaIcons.FaCartPlus />,
  //   cName: 'nav-text'
  // },
  // {
  //   title: 'Team',
  //   path: '/home',
  //   icon: <IoIcons.IoMdPeople />,
  //   cName: 'nav-text'
  // },
  // {
  //   title: 'Messages',
  //   path: '/home',
  //   icon: <FaIcons.FaEnvelopeOpenText />,
  //   cName: 'nav-text'
  // },
  // {
  //   title: 'Support',
  //   path: '/home',
  //   icon: <IoIcons.IoMdHelpCircle />,
  //   cName: 'nav-text'
  // },
  {
    title: 'Log Out',
    path: '/',
    icon: <AiIcons.AiOutlineLogout />,
    cName: 'nav-text'
  }
];