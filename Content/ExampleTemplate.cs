using Persistence<#package#>.Repositories;
//this is a comment to test the <#packageLC#>-lower-case-package-name
//this is a comment to test the <#packageFLUC#>-first-letter-upper-case-package-name
//this is a comment to test the <#nameLC#>-first-letter-upper-case-name

public class <#name#>Repository : BaseRepository<<#name#>Entity, <#name#>, <#name#>.SortBy, <#name#>.FilterAttribute>, I<#name#>Repository
{
    private readonly Lazy<Context> _context;
    protected override DbContext Context => _context.Value;

    public <#name#>Repository(Lazy<Context> context, IMapper mapper, ICurrentUser currentUser) : base(mapper, currentUser)
    {
        _context = context;
    }

    public async Task<IEnumerable<<#name#>>> GetByContactAsync(int contactId) =>
        await Find(i => i.Contact.ContactId.Equals(contactId));

    protected override SearchQuery<<#name#>Entity, <#name#>, <#name#>.SortBy, <#name#>.FilterAttribute> CreateSearchQuery()
    {
        return new <#name#>SearchQuery(Context, Mapper);
    }
}