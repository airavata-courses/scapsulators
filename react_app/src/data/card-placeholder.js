import React from 'react';

export const CardPlaceholderData = [
  {
    title: 'Reflectivity',
    subtitle: 'Strength of signal (dBZ)',
    text: 'Tells us how dense the atmosphere was in terms of wind/precipitation based on strength of the reflected RADAR signal was in Decibels relative to Z. Due to processing-time, all radar images show what HAS happened and NOT NECESSARILY WHAT IS happening.',
    link1: 'https://www.wunderground.com/prepare/understanding-radar',
    link2: 'https://www.weather.gov/cle/Area_Radars'
  },
  {
    title: 'Velocity',
    subtitle: 'Radial-velocity of "scatterers"',
    text: '"Scatterers" causes the transmitted signal to be returned to the Radar (eg: aerosols, hydrometeors and refractive index irregularities). This measurement corresponds to how fast these "scatterers" are moving away from the Radar',
    link1: 'https://wx.erau.edu/faculty/mullerb/Wx365/Doppler_velocity/radial_velocity.html',
    link2: 'https://www.weather.gov/cle/Area_Radars'
  },
  {
    title: 'Spectrum-width',
    subtitle: 'Doppler Spectrum-width',
    text: 'Tells us how fast moisture particles are moving in atmosphere. Set of particles grouped together form one pixel on Volume-scan. Can be used to locate the center pixel of a Tornado-Vortex-Signature.',
    link1: 'https://www.theweatherprediction.com/habyhints/245/',
    link2: 'https://apollo.nvu.vsc.edu/classes/remote/lecture_notes/radar/doppler/spectrum_width.html'
  }
];