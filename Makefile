lastModifiedpyFile = $(shell ls -rt *\.py* | tail -1)
compile: $(lastModifiedpyFile)
		python3 $(lastModifiedpyFile) < input 
