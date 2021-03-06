import kachery as ka

class Analysis:
    def __init__(self):
        super().__init__()

    def javascript_state_changed(self, prev_state, state):
        self._set_status('running', 'Running Analysis')

        path = state.get('path', None)
        studySetsPath = state.get('studySetsPath', None)
        if path is not None:
            self._set_status('running', 'Loading object: {}'.format(path))
            obj = ka.load_object(path=path, fr='default_readonly')
            if not obj:
                self._set_error('Unable to load object: {}'.format(path))
        elif studySetsPath is not None:
            self._set_status('running', 'Loading object: {}'.format(studySetsPath))
            obj = ka.load_object(path=studySetsPath, fr='default_readonly')
            if not obj:
                self._set_error('Unable to load object: {}'.format(path))
        else:
            self._set_error('Missing required prop: path or studySetsPath')
            return
        
        
        
        # delete this because it takes a long time to transfer
        if 'StudyAnalysisResults' in obj:
            del obj['StudyAnalysisResults']
        
        self._set_state(
            object=obj
        )

        self._set_status('finished', 'Finished Analysis')

    def _set_state(self, **kwargs):
        self.set_state(kwargs)
    
    def _set_error(self, error_message):
        self._set_status('error', error_message)
    
    def _set_status(self, status, status_message=''):
        self._set_state(status=status, status_message=status_message)