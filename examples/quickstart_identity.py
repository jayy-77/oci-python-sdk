import oci


def main() -> None:
    config = oci.config.from_file()
    oci.config.validate_config(config)

    identity = oci.identity.IdentityClient(config)
    tenancy_id = config["tenancy"]

    compartments = identity.list_compartments(
        compartment_id=tenancy_id,
        compartment_id_in_subtree=True,
        access_level="ACCESSIBLE",
    ).data

    print("Accessible compartments:")
    for c in compartments:
        print(f"- {c.name} ({c.id})")


if __name__ == "__main__":
    main()

