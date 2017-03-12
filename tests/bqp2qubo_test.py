import sys, os, pytest, json

# python 2
#from cStringIO import StringIO
# python 3
import io

#sys.path.append('.')
import bqpjson.bqp2qubo as bqp2qubo
import bqpjson.spin2bool as spin2bool

from common_test import valid_spin_bqp_files
from common_test import valid_bool_bqp_files

@pytest.mark.parametrize('bqp_file', valid_spin_bqp_files)
def test_bqp2qh_spin(bqp_file, capsys):
    with open(bqp_file.replace('.json', '.qubo'), 'r') as file:
        base = file.read()

    with open(bqp_file, 'r') as file:
        data_spin = json.load(file)

    data_bool = spin2bool.swap_variable_domain(data_spin)

    # python 2
    #data_stream = StringIO(json.dumps(data_bool))
    # python 3
    data_stream = io.StringIO(json.dumps(data_bool))

    bqp2qubo.main(None, data_stream)

    out, err = capsys.readouterr()

    assert(out.strip() == base.strip())


@pytest.mark.parametrize('bqp_file', valid_bool_bqp_files)
def test_bqp2qh_bool(bqp_file, capsys):
    with open(bqp_file.replace('.json', '.qubo'), 'r') as file:
        base = file.read()

    with open(bqp_file, 'r') as file:
        data_bool = json.load(file)

    # python 2
    #data_stream = StringIO(json.dumps(data_bool))
    # python 3
    data_stream = io.StringIO(json.dumps(data_bool))

    bqp2qubo.main(None, data_stream)

    out, err = capsys.readouterr()

    assert(out.strip() == base.strip())