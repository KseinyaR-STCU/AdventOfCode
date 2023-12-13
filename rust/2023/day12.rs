#[path = "../modules/files.rs"]
mod files;

use std::collections::HashMap;
use std::env;

fn get_file() -> String {
    return if let Some(_arg1) = env::args().nth(1) {
        "full.txt".to_string()
    } else {
        "test.txt".to_string()
    };
}

fn main() {
    let values: Vec<String> = files::read_lines(get_file())
        .unwrap()
        .map(|line| line.unwrap())
        .collect();

    part1(&values);
    part2(&values);
}

fn part1(values: &Vec<String>) {
    let mut total = 0;
    for v in values {
        let (springs, counts) = get_parsed_part_1(&v);
        let count = count_options(&springs, &counts);
        total += count;
    }
    println!("part 1: {}", total);
}

fn part2(values: &Vec<String>) {
    let mut total = 0;
    for v in values {
        let (springs, counts) = get_parsed_part_2(&v);
        let count = count_options(&springs, &counts);
        total += count;
    }
    println!("part 2: {}", total);
}

fn get_parsed_part_1(value: &String) -> (String, Vec<usize>) {
    let (springs, counts) = parse(value);
    return (springs, counts);
}

fn get_parsed_part_2(value: &String) -> (String, Vec<usize>) {
    let (springs_0, counts_0) = parse(value);
    let (springs, counts) = times_five(springs_0, counts_0);
    return (springs, counts);
}

fn count_options(springs: &String, counts: &Vec<usize>) -> usize {
    let starting_value: Vec<usize> = vec![];

    let mut cache = HashMap::new();

    return create_all_options(starting_value, &springs, &counts, &mut cache);
}

fn create_cache_key(created_value: &Vec<usize>, orig_value: &String) -> String {
    let created_joined = created_value
        .iter()
        .map(|x| x.to_string())
        .collect::<Vec<String>>()
        .join(",");
    let orig_value_len = orig_value.len();
    return format!("{created_joined}-{orig_value_len}");
}

fn create_all_options(
    created_value: Vec<usize>,
    orig_value: &String,
    counts: &Vec<usize>,
    cache: &mut HashMap<String, usize>,
) -> usize {
    let mut all_options_count = 0;

    let cache_key = create_cache_key(&created_value, &orig_value);

    if let Some(&ref x) = cache.get(&cache_key) {
        return *x;
    }

    if !is_possibly_valid(created_value.clone(), orig_value, counts) {
        cache.insert(cache_key.to_owned(), all_options_count);
        return all_options_count;
    }

    if orig_value.len() == 0 {
        all_options_count += 1;
        return all_options_count;
    }

    let mut mutable_created_value = created_value.clone();
    if mutable_created_value.len() == 0 {
        mutable_created_value.push(0);
    }
    
    if orig_value.contains('#') || orig_value.contains('?') {
        //only questions left, see if we made it
        if !orig_value.contains('#') {
            all_options_count +=
                create_all_options(mutable_created_value.clone(), &"".to_owned(), counts, cache);
        }

        let (v, og_subset) = split_into_first_and_subset(&orig_value);

        if v == '?' {
            let mut with_dot = mutable_created_value.clone();
            if *with_dot.last().unwrap() != 0 {
                with_dot.push(0);
            }
            all_options_count += create_all_options(with_dot, &og_subset, counts, cache);

            let mut with_hash = mutable_created_value.clone();
            with_hash[mutable_created_value.len() - 1] += 1;
            all_options_count += create_all_options(with_hash, &og_subset, counts, cache);
        } else if v == '.' {
            let mut with_dot = mutable_created_value.clone();
            if *with_dot.last().unwrap() != 0 {
                with_dot.push(0);
            }
            all_options_count += create_all_options(with_dot, &og_subset, counts, cache);
        } else {
            let mut with_hash = mutable_created_value.clone();
            with_hash[mutable_created_value.len() - 1] += 1;
            all_options_count += create_all_options(with_hash, &og_subset, counts, cache);
        }
    } else {
        //Only dots left, check if it made it
        all_options_count +=
            create_all_options(mutable_created_value, &"".to_owned(), counts, cache);
    }

    cache.insert(cache_key.to_owned(), all_options_count);
    return *cache.get(&cache_key).unwrap();
}

fn split_into_first_and_subset(orig_value: &String) -> (char, String) {
    let v = orig_value.as_bytes()[0] as char;
    let og_subset = orig_value[1..].to_owned();
    return (v, og_subset);
}

fn is_possibly_valid(options: Vec<usize>, orig_value: &String, counts: &Vec<usize>) -> bool {
    if options.len() == 0 {
        return true;
    }

    let is_last_option = orig_value.len() == 0;

    let current_count = options.iter().sum::<usize>();
    let current_count_with_spacers = current_count + options.len() - 1;
    let min_count_needed = counts.iter().sum::<usize>() + counts.len() - 1;

    if current_count_with_spacers + orig_value.len() < min_count_needed {
        return false;
    }

    return check_sections(&options, counts, is_last_option);
}

fn check_sections(section_lengths: &Vec<usize>, counts: &Vec<usize>, is_last_option: bool) -> bool {
    if section_lengths.len() > counts.len() {
        return false;
    }

    for (i, s) in section_lengths.iter().enumerate() {
        if *s > counts[i] {
            return false;
        } else if *s < counts[i] {
            if i != section_lengths.len() - 1 || is_last_option {
                return false;
            }
        }
    }
    return true;
}

fn parse(values: &String) -> (String, Vec<usize>) {
    let (springs, counts) = values.split_once(' ').unwrap();

    let sections: Vec<String> = springs
        .split('.')
        .collect::<Vec<&str>>()
        .iter()
        .filter(|&x| x != &"")
        .map(|&x| x.to_string())
        .collect();

    let count_nums = counts
        .split(',')
        .collect::<Vec<&str>>()
        .iter()
        .map(|&x| x.parse::<usize>().unwrap())
        .collect();

    let separator = ".";

    let mut new_spring = sections.join(separator);

    if springs.starts_with(".") {
        new_spring = format!("{separator}{new_spring}");
    }

    if springs.ends_with(separator) {
        new_spring = format!("{new_spring}{separator}");
    }

    (new_spring, count_nums)
}

fn times_five(springs: String, values: Vec<usize>) -> (String, Vec<usize>) {
    let mut new_springs = "".to_owned();
    let mut new_values = vec![];

    for i in 0..5 {
        new_springs.push_str(&springs);
        new_values.extend(&values);
        if i != 4 {
            new_springs.push_str("?");
        }
    }
    return (new_springs, new_values);
}
