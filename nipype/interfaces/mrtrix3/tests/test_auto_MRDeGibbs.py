# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import MRDeGibbs


def test_MRDeGibbs_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        axes=dict(
            argstr='-axes %s',
            maxlen=2,
            minlen=2,
            sep=',',
            usedefault=True,
        ),
        bval_scale=dict(argstr='-bvalue_scaling %s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        grad_file=dict(argstr='-grad %s', ),
        grad_fsl=dict(argstr='-fslgrad %s %s', ),
        in_bval=dict(),
        in_bvec=dict(argstr='-fslgrad %s %s', ),
        in_file=dict(
            argstr='%s',
            mandatory=True,
            position=-2,
        ),
        maxW=dict(
            argstr='-maxW %d',
            usedefault=True,
        ),
        minW=dict(
            argstr='-minW %d',
            usedefault=True,
        ),
        nshifts=dict(
            argstr='-nshifts %d',
            usedefault=True,
        ),
        nthreads=dict(
            argstr='-nthreads %d',
            nohash=True,
        ),
        out_file=dict(
            argstr='%s',
            genfile=True,
            keep_extension=True,
            name_source='in_file',
            name_template='%s_unr',
            position=-1,
        ),
    )
    inputs = MRDeGibbs.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_MRDeGibbs_outputs():
    output_map = dict(out_file=dict(), )
    outputs = MRDeGibbs.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
