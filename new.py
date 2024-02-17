def get_changes(repo, a_blob, b_blob):
    if a_blob is None:
        return repo.git.show(b_blob)

    lines_a = repo.git.show(a_blob).splitlines()
    lines_b = repo.git.show(b_blob).splitlines()

    differ = difflib.Differ()
    diff = differ.compare(lines_a, lines_b)

    changed_lines = []
    for line in diff:
        if line.startswith('- '):
            changed_lines.append(f"{line[2:]}")
        elif line.startswith('+ '):
            changed_lines.append(f"{line[2:]}")

    return '\n'.join(changed_lines)

