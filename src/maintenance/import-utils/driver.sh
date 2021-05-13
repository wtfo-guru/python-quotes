#!/bin/bash

EXT=.utf8.converted

if [ ! -f downloads/unique.quotes ]
then
  for fn in $(ls downloads/random.quotes.*)
  do
    # CV="${fn}${EXT}"
    # echo $fn
    # iconv -t UTF-8//TRANSLIT "$fn" -o "$CV"
    # RC=$?
    # if [[ "$RC" != "0" ]]
    # then
    #   exit $RC
    # fi
    cat "$fn" >> downloads/combined.quotes
  done

  cat combined.quotes | sort | uniq -u > downloads/unique.quotes
fi

iconv -t UTF-8//TRANSLIT "downloads/unique.quotes" -o "downloads/unique.quotes${EXT}"
