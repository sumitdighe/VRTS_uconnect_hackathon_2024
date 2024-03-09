import React from 'react';
import { ReactLenis, useLenis } from '@studio-freight/react-lenis';

const SmoothScrollWrapper = ({ children }) => {
  const lenis = useLenis(({ scroll }) => {
    // called every scroll
    console.log('Scrolled:', scroll);
  });

  return <ReactLenis root>{children}</ReactLenis>;
};

export default SmoothScrollWrapper;
