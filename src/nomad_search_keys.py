import yaml

from nomad.datamodel import EntryArchive
from nomad.metainfo import Reference, MEnum
from nomad.metainfo.elasticsearch_extension import entry_index

if __name__ == '__main__':
    data = dict()
    entry_index.doc_type.create_mapping(EntryArchive.m_def)
    for key, value in entry_index.doc_type.quantities.items():
        annotation = value.annotation

        try:
            if isinstance(annotation.definition.type, Reference):
                continue

            if isinstance(annotation.definition.type, MEnum):
                type = list(annotation.definition.type)
            else:
                type = annotation.definition.type.__name__
        except:
            type = str(annotation.definition.type)

        if annotation.field:
            key = f'{key}.{annotation.field}'

        data[key] = dict(
            repeats=value.repeats,
            description=annotation.definition.description,
            type=type
        )
    print(yaml.dump(data))