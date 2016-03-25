net_inv_etree.py

```
FPC: 0 -- MPC-3D-16XGE-SFPP-X

        PIC: 0
                0/0 - 0/0
                0/1 - 0/1
                0/2 - Free
                0/3 - Free

FPC: 1 -- MPC-3D-16XGE-SFPP-X

        PIC: 0
                0/0 - 0/0
                0/1 - 0/1
                0/2 - Free
                0/3 - Free

        PIC: 1
                1/0 - 1/0
                1/1 - Free
                1/2 - Free
                1/3 - Free

        PIC: 2
                2/0 - Free
                2/1 - Free
                2/2 - Free
                2/3 - 2/3

        PIC: 3
                3/0 - Free
                3/1 - 3/1
                3/2 - Free
                3/3 - 3/3
```

inventory_opt (merged)

```json
{
    '0': {
        '0': ['0/0', '0/1'],
        'model': 'MPC-3D-16XGE-SFPP-X',
        'serial': 'CW0213093063'},
    '1': {
        '0': ['0/0', '0/1'],
        '1': ['1/0'],
        '2': ['2/3'],
        '3': ['3/1', '3/3'],
        'model': 'MPC-3D-16XGE-SFPP-X',
        'serial': 'CW0213093063'}
}

```

inventory_fpc

```json
{
    '0': {
        'model': 'MPC-3D-16XGE-SFPP-X', 
        'serial': 'CW0213093063'
    },
    '1': {
        'model': 'MPC-3D-16XGE-SFPP-X', 
        'serial': 'CW0213093063'}
}

```

inventory_opt

```json
{
    '0': {
        '0': ['0/0', '0/1']},
    '1': {
        '0': ['0/0', '0/1'], 
        '1': ['1/0'], 
        '2': ['2/3'], 
        '3': ['3/1', '3/3']
    }
}

```
