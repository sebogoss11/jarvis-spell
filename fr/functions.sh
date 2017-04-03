#!/bin/bash

jv_spell_spell()
{
	python -u ~/jarvis/plugins/jarvis-spell/python/spell.py
	while read line
	do
		say "$line"
	done < ~/jarvis/plugins/jarvis-spell/python/spell.txt
}
