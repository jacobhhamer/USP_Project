#!/bin/sh

wget "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&select=kepid,kepler_name,koi_disposition, koi_score,koi_period,koi_sma,ra,dec,koi_kepmag,&where=koi_period<1&where=koi_disposition like 'CANDIDATE'&where=koi_disposition like 'CONFIRMED'&order=kepid&format=csv" -O "DR25USPs.txt"