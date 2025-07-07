import argparse
import sys
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from Passive_Design_Consultant import PassiveDesignConsultant  # Adjust if class name is different

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, default="0 - 0.5 m/s")
    parser.add_argument('--comf', type=int, default=1)
    parser.add_argument('--epw', type=int, default=1)
    parser.add_argument('--evap', type=int, default=1)
    parser.add_argument('--thm', type=int, default=1)
    parser.add_argument('--sun', type=int, default=1)
    parser.add_argument('--custom_dbt', type=str, default="0")
    parser.add_argument('--custom_rh', type=str, default="0")
    parser.add_argument('--evap_efficiency', type=int, default=80)
    args = parser.parse_args()

    # Convert stringified lists if needed
    custom_dbt = json.loads(args.custom_dbt) if args.custom_dbt != "0" else 0
    custom_rh = json.loads(args.custom_rh) if args.custom_rh != "0" else 0

    # Instantiate your class and set required attributes
    consultant = PassiveDesignConsultant()
    # You may need to set dbt, rh, elevation, etc. on the consultant object here

    # Generate the psychrometric graph (should plot to current figure)
    consultant.psychrometric_graph(
        text=args.text,
        comf=args.comf,
        epw=args.epw,
        evap=args.evap,
        thm=args.thm,
        sun=args.sun,
        custom_dbt=custom_dbt,
        custom_rh=custom_rh,
        evap_efficiency=args.evap_efficiency
    )

    # Save the current figure to SVG and print to stdout
    import io
    buf = io.StringIO()
    plt.savefig(buf, format='svg')
    buf.seek(0)
    print(buf.read())

if __name__ == '__main__':
    main()
